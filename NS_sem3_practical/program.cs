using System;

public class Person
{
    // Private fields (attributes) encapsulated within the class
    private string name;
    private int age;

    // Public methods to access and manipulate the private data
    // These methods are part of the encapsulation
    public void SetName(string newName)
    {
        // Validation can be added here if needed
        name = newName;
    }

    public string GetName()
    {
        return name;
    }

    public void SetAge(int newAge)
    {
        // Validation can be added here if needed
        age = newAge;
    }

    public int GetAge()
    {
        return age;
    }
}

class program
{
    static void Main()
    {
        // Create an instance of the Person class
        Person person = new Person();

        // Use the public methods to set and get data
        person.SetName("John Doe");
        person.SetAge(25);

        // Access the data only through the public methods
        Console.WriteLine($"Name: {person.GetName()}");
        Console.WriteLine($"Age: {person.GetAge()}");
    }
}
