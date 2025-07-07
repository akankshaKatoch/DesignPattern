package com.example;

public class EmployeeReportGenerator {
    // Separate class for report generation as per SRP
    public void generateReport(Employee employee) {
        System.out.println("Employee Report: " + employee.getName() + " - " + employee.getPosition());
    }
}

