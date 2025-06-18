import os
import openai

def main():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        print("Error: Please set your OPENAI_API_KEY environment variable.")
        return

    while True:
        prompt = input("Enter prompt (or type 'quit' to exit): ").strip()
        if prompt.lower() == 'quit':
            print("Goodbye!")
            break
        if not prompt:
            print("Prompt cannot be empty.")
            continue

        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=150
            )
            print("\nAI response:")
            print(response.choices[0].message.content.strip())
        except Exception as e:
            print(f"API error: {e}")

if __name__ == "__main__":
    main()


