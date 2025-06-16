import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def get_summary(query):
    try:
        wikipedia.set_lang("en")
        print("🔍 Searching for:", query)
        results = wikipedia.search(query)

        if not results:
            return "❌ No results found."

        try:
            return wikipedia.summary(results[0], sentences=2)

        except DisambiguationError as e:
            print(f"⚠️ Disambiguation: Picking first option from: {e.options[:3]}")
            return wikipedia.summary(e.options[0], sentences=2)

    except PageError:
        return "❌ Page not found."
    except Exception as e:
        return f"💥 Unknown error: {e}"