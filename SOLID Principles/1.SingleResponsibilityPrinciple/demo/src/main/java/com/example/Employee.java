package com.example;
public class Employee {
    private String name;
    private String position;

    public Employee(String name, String position) {
        this.name = name;
        this.position = position;
    }

    public String getName() {
        return name;
    }

    public String getPosition() {
        return position;
    }
}

/*
// Separate class for report generation as per SRP
class EmployeeReportGenerator {
    public void generateReport(Employee employee) {
        System.out.println("Employee Report: " + employee.getName() + " - " + employee.getPosition());
    }
}
*/