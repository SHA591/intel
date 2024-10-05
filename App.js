import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
    const [droneData, setDroneData] = useState([]);

    useEffect(() => {
        const fetchDroneData = async () => {
            const response = await axios.get('http://127.0.0.1:5000/drones');
            setDroneData(response.data);
        };

        fetchDroneData();
        const interval = setInterval(fetchDroneData, 5000); // Poll every 5 seconds
        return () => clearInterval(interval);
    }, []);

    return (
        <div>
            <h1>Drone Dashboard</h1>
            <ul>
                {droneData.map((drone, index) => (
                    <li key={index}>{drone}</li>
                ))}
            </ul>
        </div>
    );
}

export default App;
