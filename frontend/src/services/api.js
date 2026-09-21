const API_URL = "http://127.0.0.1:8000";

export async function askAI(question) {
    const response = await fetch(`${API_URL}/chat`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            question: question,
        }),
    });

    const data = await response.json();
    return data;
}