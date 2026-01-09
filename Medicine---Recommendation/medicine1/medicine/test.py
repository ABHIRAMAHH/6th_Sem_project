from google import genai

client = genai.Client(api_key="AIzaSyDIKeho82uzNRnpQi_G1zu-Jj9s97dwbJk")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="previous symptoms were itching,skin_rash,nodal_skin_eruptions the diagnosis was fungal infection, after giving medication no changes were there in the health condition, give another diagnosis",
)

print(response.text)