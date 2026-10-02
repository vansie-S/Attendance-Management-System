function SummaryCards({ attendance }) {
    const totalRecords = attendance.length;

    const presentCount = attendance.filter(
        (record) => record.status === "Present"
    ).length;

    const studentsRecognized = new Set(
        attendance.map((record) => record.studentId)
    ).size;

    return (
        <div className="summary-container">
            <div className="summary-card">
                <h3>Total Records</h3>
                <p>{totalRecords}</p>
            </div>

            <div className="summary-card">
                <h3>Present</h3>
                <p>{presentCount}</p>
            </div>

            <div className="summary-card">
                <h3>Students Recognized</h3>
                <p>{studentsRecognized}</p>
            </div>
        </div>
    );
}

export default SummaryCards;