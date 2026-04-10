// Example backend (e.g., server.js using Express)
import express from "express";
import dotenv from "dotenv";
import morgan from "morgan";
import cors from 'cors';
const oaikey = '';


dotenv.config(); // Load environment variables (OPENAI_API_KEY)
const app = express();
app.use(express.json()); // If needed for other routes
app.use(morgan('dev'));
app.use(cors());

// Endpoint to mint an ephemeral token
app.get("/rtapi/session", async (req, res) => {
  // You might want to associate this session with your interview ID (`req.params.id`)
  // or pass specific initial instructions/context in the body if the API supports it.
  const model = "gpt-4o-realtime-preview-2024-12-17"; // Or your desired model
  const voice = "verse"; // Choose a voice

  try {
    const response = await fetch("https://api.openai.com/v1/realtime/sessions", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${oaikey}`, // Use your STANDARD key securely here
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        model: model,
        voice: voice,
        // Add any other session configuration here if needed
      }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      console.error("Error fetching ephemeral token:", errorData);
      return res
        .status(response.status)
        .json({ error: "Failed to create Realtime session" });
    }

    const data = await response.json();
    console.log("Sending ephemeral token to client:", data.client_secret?.value?.substring(0, 10) + "..."); // Log masked token
    res.json(data); // Send the entire session object back, including the ephemeral key
  } catch (error) {
    console.error("Server error:", error);
    res.status(500).json({ error: "Internal server error" });
  }
});

// Add your other API endpoints (like /api/converse which might now be used less, or for setup/teardown)

const PORT = process.env.PORT || 3001; // Use a different port if your frontend is on 3000
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
