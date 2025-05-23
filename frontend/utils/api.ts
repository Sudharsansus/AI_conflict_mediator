const BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL;

export const analyzeConflict = async (message: string) => {
  const response = await fetch(`${BASE_URL}/api/analyze`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message }),
  });
  return response.json();
};
