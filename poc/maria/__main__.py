# from transformers import AutoModelForMaskedLM
# from transformers import AutoTokenizer, FillMaskPipeline
# from pprint import pprint
# tokenizer_hf = AutoTokenizer.from_pretrained('PlanTL-GOB-ES/roberta-base-bne')
# model = AutoModelForMaskedLM.from_pretrained('PlanTL-GOB-ES/roberta-base-bne')
# model.eval()
# pipeline = FillMaskPipeline(model, tokenizer_hf)
# text = f"¡Hola <mask>!"
# res_hf = pipeline(text)
# pprint([r['token_str'] for r in res_hf])

import tensorflow as tf
from transformers import TFAutoModelForSequenceClassification

# from transformers import DefaultDataCollator
# from transformers import AutoTokenizer

# from datasets import load_dataset, DatasetDict, Dataset
# dataset = load_dataset("yelp_review_full")
# print(dataset["train"][0])
# dataset = DatasetDict(
#     {
#         "train": Dataset({"features": ["label", "text"], "num_rows": 4}),
#         "test": Dataset({"features": ["label", "text"], "num_rows": 4}),
#     }
# )
train_dataset = [
    {"label": 1, "text": "perro"},
    {"label": 2, "text": "manzana"},
    {"label": 1, "text": "elefante"},
    {"label": 2, "text": "pera"},
]
test_dataset = [
    {"label": 1, "text": "gato"},
    {"label": 2, "text": "sandía"},
    {"label": 1, "text": "ratón"},
    {"label": 2, "text": "melón"},
]

# print(dataset.data)

# print(dataset)
# print(dataset["train"][0])

# tokenizer = AutoTokenizer.from_pretrained("PlanTL-GOB-ES/roberta-base-bne")


# def tokenize_function(examples):
#     return tokenizer(examples["text"], padding="max_length", truncation=True)


# tokenized_train_dataset = train_dataset.map(tokenize_function, batched=True)
# tokenized_test_dataset = test_dataset.map(tokenize_function, batched=True)

# small_train_dataset = tokenized_train_dataset.shuffle(seed=42).select(range(4))
# small_eval_dataset = tokenized_test_dataset.shuffle(seed=42).select(range(4))

# data_collator = DefaultDataCollator(return_tensors="tf")

# tf_train_dataset = small_train_dataset.to_tf_dataset(
#     columns=["attention_mask", "input_ids", "token_type_ids"],
#     label_cols=["labels"],
#     shuffle=True,
#     collate_fn=data_collator,
#     batch_size=8,
# )

# tf_validation_dataset = small_eval_dataset.to_tf_dataset(
#     columns=["attention_mask", "input_ids", "token_type_ids"],
#     label_cols=["labels"],
#     shuffle=False,
#     collate_fn=data_collator,
#     batch_size=8,
# )


# model = TFAutoModelForSequenceClassification.from_pretrained(
#     "PlanTL-GOB-ES/roberta-base-bne", num_labels=5
# )

model = TFAutoModelForSequenceClassification.from_pretrained(
    "PlanTL-GOB-ES/roberta-base-bne",
    from_pt=True
)  # Download model and configuration from S3 and cache.


model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=5e-5),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=tf.metrics.SparseCategoricalAccuracy(),
)

model.fit(train_dataset, validation_data=test_dataset, epochs=3)

model.predict("sapo")
