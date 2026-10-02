package com.attendance.attendance_backend;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;
import java.time.LocalDate;

public interface AttendanceRepository extends JpaRepository<Attendance, Integer> {  List<Attendance> findByStudentId(Integer studentId);
    List<Attendance> findByDate(LocalDate date);

}
