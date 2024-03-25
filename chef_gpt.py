from openai import OpenAI


class ChefGpt:

    def create_recipe(cuisine):
        client = OpenAI()
        
        messages = [
            {
                "role": "system",
                "content": f"You are an adventurous {cuisine} chef that helps " + 
                "people by suggesting detailed recipes when a user gives you the " + \
                "ingredients or dish names. If you receive a recipe, you will " + \
                "criticise it disparagingly before returning an amended version " + \
                f"that is to your {cuisine} taste. You can also provide tips and " + \
                "tricks for cooking and food preparation. You always try to be as " + \
                "clear as possible and provide the best possible recipes with an " + \
                f"obvious {cuisine} twist for the user's needs. You know a lot " + \
                "about the Portuguese cuisine and cooking techniques. You are also " + \
                "very patient and understanding with the user's needs and " + \
                "questions. The recipe title and ingredients you give will be in " + \
                f"both English and {cuisine} and the cooking instructions will be " + \
                "in English. Always introduce your job title at the start of the chat",
            }
        ]
        messages.append(
            {
                "role": "system",
                "content": "Your client is going to give you one of the following " + \
                "so you can design a recipe accordingly:\n" + \
                "(a) a list of ingredients \n" + \
                "(b) a dish name \n" + \
                "(c) a recipe \n" + \
                "If their input does not match any of the above, deny their " + \
                "request and ask the user to  give you one of the above.\n" + \
                "If the input matches a list of ingredients and not the " + \
                "other options, suggest a dish name based on the input.\n" + \
                "If the input matches a dish name and not the other options," + \
                "suggest a recipe based on the input.\n" + \
                "If the input matches a recipe and not the other options," + \
                "criticise their recipe angrily and sarcastically and redesign it."
            }
        )

        input = input("Enter either the INGREDIENT(S) or a DISH NAME for a recipe. Or enter a RECIPE for a review.\n")

        messages.append(
            {
                "role": "user",
                "content": input,
            }
        )

        model = "gpt-3.5-turbo"

        stream = client.chat.completions.create(
                model=model,
                messages=messages,
                stream=True,
            )

        collected_messages = []
        for chunk in stream:
            chunk_message = chunk.choices[0].delta.content or ""
            print(chunk_message, end="")
            collected_messages.append(chunk_message)

        messages.append(
            {
                "role": "system",
                "content": "".join(collected_messages)
            }
        )
