import tensorflow as tf
import numpy as np
import sklearn
from sklearn import metrics
import transformers
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
import json
import matplotlib.pyplot as plt
import random
import seaborn as sn

# detect and init the TPU
# tpu = tf.distribute.cluster_resolver.TPUClusterResolver()
# tf.config.experimental_connect_to_cluster(tpu)
# tf.tpu.experimental.initialize_tpu_system(tpu)
# tpu_strategy = tf.distribute.experimental.TPUStrategy(tpu)

# batch_size=32 * tpu_strategy.num_replicas_in_sync
# print('Batch size:', batch_size)
# AUTOTUNE = tf.data.experimental.AUTOTUNE

# Load data from json file
# data = [json.loads(line) for line in open('./News_Category_Dataset_v2.json', 'r')]
data = [
    {"label": 1, "text": "perro"},
    {"label": 2, "text": "manzana"},
    {"label": 1, "text": "elefante"},
    {"label": 2, "text": "pera"},
]
random.shuffle(data)  # shuffle the data
labels = []
# headlines=[]
texts = []
for line in data:
    labels.append(line["label"])
    # headlines.append(line['headline'])
    # Combine headline and description into a single text input
    # text=line['headline']+' '+line['short_description']
    texts.append(line["text"])

tokenizer = AutoTokenizer.from_pretrained("roberta-base")  # Tokenizer
inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="tf")  # Tokenized text
print(inputs)

# dataset=tf.data.Dataset.from_tensor_slices((dict(inputs), indices)) #Create a tensorflow dataset
# #train test split, we use 10% of the data for validation
# val_data_size=int(0.1*n_elements)
# val_ds=dataset.take(val_data_size).batch(batch_size, drop_remainder=True)
# train_ds=dataset.skip(val_data_size).batch(batch_size, drop_remainder=True)
# train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)
base = "PlanTL-GOB-ES/roberta-base-bne"
# base = "roberta-base"
model = TFAutoModelForSequenceClassification.from_pretrained(base, num_labels=2)
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-5, clipnorm=1.0),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=[
        tf.metrics.SparseCategoricalAccuracy(),
        tf.keras.metrics.SparseTopKCategoricalAccuracy(
            k=3, name="Sparse_Top_3_Categorical_Accuracy"
        ),
    ],
)

# history=model.fit(train_ds, validation_data=val_ds, epochs=6, verbose=1)
