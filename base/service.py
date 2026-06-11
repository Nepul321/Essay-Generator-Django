from google import genai
from django.conf import settings
import markdown

client = genai.Client(api_key=settings.GEMINI_API_KEY)


def ask_gemini(prompt, paragraphs, level):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
                    Answer clearly using markdown.

                    Use:
                    - headings
                    - bullet points
                    - short paragraphs
                    - code blocks if needed

                    Generate an essay on the prompt : {prompt}, and {paragraphs} paragraphs.
                    Make sure that the essay is at the {level} grade level.
                    If grade level unclear, make sure the essay fits 12th grade or higher standards.


            """
        )
        
        markdown_text = response.text
        html = markdown.markdown(markdown_text)

        return {
          "markdown" : markdown_text,
          "html" : html
        }

    except Exception as e:
        return f"Gemini error: {str(e)}"