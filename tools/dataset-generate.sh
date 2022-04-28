aws lambda invoke --function-name tfm-$1-dataset-generate dataset.json
cat dataset.json
echo ""