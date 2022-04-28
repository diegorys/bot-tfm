aws lambda invoke --function-name tfm-$1-dataset-generate response.json
cat dataset.csv
echo ""