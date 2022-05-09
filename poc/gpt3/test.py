import openai
print(1)

fine_tuned_model = "davinci:ft-personal-2022-05-09-18-43-18"
print(2)
openAIResponse = openai.Completion.create(
    model=fine_tuned_model,
    prompt="Me tengo que tomar las pastillas de la alergia el martes a las cuatro de la tarde.",
    stop=["Ej", "Command"]
)
print(3)

command = openAIResponse["choices"][0]["text"].strip()
print("response")
print(command)
