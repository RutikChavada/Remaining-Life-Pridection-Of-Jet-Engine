const API_URL = "http://localhost:5000";

export const startGeneration = async () => {
    const response = await fetch(`${API_URL}/start`, { method: "POST" });
    return response.json();
};

export const stopGeneration = async () => {
    const response = await fetch(`${API_URL}/stop`, { method: "POST" });
    return response.json();
};

export const fetchSensorData = async () => {
    const response = await fetch(`${API_URL}/fetch`);
    return response.json();
};
