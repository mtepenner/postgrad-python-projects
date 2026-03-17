import os
import sys
from g4f.client import Client

def process_notes_with_ai(raw_text):
    client = Client()
    print("... Asking the AI to polish your notes ...")
    
    # Prompting the AI to both format the text and provide a specific filename
    prompt = (
        f"Clean up the following notes to be more readable and professional. "
        f"Format them in Markdown. Also, start your response with a single line "
        f"containing only a suggested filename in ALL CAPS (no extension). \n\n"
        f"NOTES:\n{raw_text}"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o", # You can also try "gpt-3.5-turbo" or "claude-3-opus"
            messages=[{"role": "user", "content": prompt}]
        )
        
        full_output = response.choices[0].message.content
        # Split the first line for the title and the rest for the content
        lines = full_output.split('\n', 1)
        filename = lines[0].strip().replace(" ", "_")
        refined_content = lines[1].strip() if len(lines) > 1 else full_output
        
        return refined_content, filename
    except Exception as e:
        print(f"Error connecting to AI: {e}")
        return None, "FAILED_NOTES"

def main():
    print("--- [ AI NOTE TAKER ] ---")
    print("Enter your notes. Type 'FINISHEDNOTES' on a new line to finish.")
    
    lines = []
    while True:
        try:
            line = input()
            if "FINISHEDNOTES" in line:
                # Add anything typed before the keyword on the same line
                clean_line = line.replace("FINISHEDNOTES", "").strip()
                if clean_line:
                    lines.append(clean_line)
                break
            lines.append(line)
        except EOFError:
            break

    raw_text = "\n".join(lines)
    
    if not raw_text.strip():
        print("No notes entered. Closing.")
        return

    content, title = process_notes_with_ai(raw_text)
    
    if content:
        filename = f"{title}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"\n[DONE] Your notes have been saved to: {filename}")
    else:
        print("Failed to process notes.")

if __name__ == "__main__":
    main()
