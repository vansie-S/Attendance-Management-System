import { useEffect, useState } from "react";
import Header from "./Header";
import SummaryCards from "./SummaryCards";
import "./App.css";

function App() {
    const [attendance, setAttendance] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");
    const [selectedDate, setSelectedDate] = useState("");
    const [selectedStudent, setSelectedStudent] = useState("");

    useEffect(() => {
        fetch("http://localhost:8080/api/attendance")
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Failed to fetch attendance data");
                }

                return response.json();
            })
            .then((data) => {
                setAttendance(data);
                setLoading(false);
            })
            .catch((error) => {
                console.error("Error fetching attendance:", error);
                setError("Unable to load attendance records.");
                setLoading(false);
            });
    }, []);
    
    const filteredAttendance = attendance.filter((record) => {
        const matchesDate =
            !selectedDate ||
            String(record.date).substring(0, 10) === selectedDate;

        const matchesStudent =
            !selectedStudent ||
            String(record.studentId) === selectedStudent;

        return matchesDate && matchesStudent;
    });
    return (
        <div>
            <Header />

            <SummaryCards attendance={filteredAttendance} />

            <main className="dashboard-content">
                <h2>Attendance Dashboard</h2>

                <section className="records-section">
                    <h2>Attendance Records</h2>
                    <div className="filter-section">

                        <label htmlFor="date">Filter by Date:</label>

                        <input
                            type="date"
                            id="date"
                            value={selectedDate}
                            onChange={(e) => {

                                setSelectedDate(e.target.value);
                            }}
                        />

                        <label htmlFor="student">Student ID:</label>

                        <input
                            type="number"
                            id="student"
                            placeholder="Enter Student ID"
                            value={selectedStudent}
                            onChange={(e) => setSelectedStudent(e.target.value)}
                        />

                        <button
                            onClick={() => {
                                setSelectedDate("");
                                setSelectedStudent("");
                            }}
                        >
                            Show All
                        </button>

                    </div>

                    {loading && (
                        <p>Loading attendance records...</p>
                    )}

                    {error && (
                        <p>{error}</p>
                    )}

                    {!loading && !error && filteredAttendance.length === 0 && (
                        <p>No attendance records found for this date.</p>
                    )}

                    {!loading && !error && filteredAttendance.length > 0 && (
                        <div className="table-container">
                            <table>
                                <thead>
                                <tr>
                                    <th>Student ID</th>
                                    <th>Date</th>
                                    <th>Time</th>
                                    <th>Status</th>
                                </tr>
                                </thead>

                                <tbody>
                                {filteredAttendance.map((record) => (
                                    <tr key={record.attendanceId}>
                                        <td>{record.studentId}</td>
                                        <td>{record.date}</td>
                                        <td>{record.time}</td>
                                        <td>{record.status}</td>
                                    </tr>
                                ))}
                                </tbody>
                            </table>
                        </div>
                    )}
                </section>
            </main>
        </div>
    );
}

export default App;
