# echo $payload
aws lambda invoke --function-name tfm-$1-dataset-update --payload fileb://dataset.json response.json
# cat output.json
echo ""