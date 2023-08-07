#include <iostream>
#include <string>

using namespace std;

// Author class definition
class Author {
private:
    string name;
    string email;
    char gender;

public:
    // Constructor to initialize Author object
    Author(string name, string email, char gender) : name(name), email(email), gender(gender) {}

    // Getter methods for name, email, and gender
    string getName() const {
        return name;
    }

    string getEmail() const {
        return email;
    }

    // Setter method for email
    void setEmail(string email) {
        this->email = email;
    }

    // Getter method for gender
    string getGender() const {
        return (gender == 'm' || gender == 'M') ? "male" : "female";
    }

    // Print method to display Author's information
    string print() const {
        return name + " (" + getGender() + ") at " + email;
    }
};

// Book class definition
class Book {
private:
    string name;
    Author author;
    double price;

public:
    // Constructor to initialize Book object
    Book(string name, Author author, double price) : name(name), author(author), price(price) {}

    // Getter methods for name, author, and price
    string getName() const {
        return name;
    }

    Author getAuthor() const {
        return author;
    }

    double getPrice() const {
        return price;
    }

    // Setter method for price
    void setPrice(double price) {
        this->price = price;
    }

    // Print method to display Book's information
    string print() const {
        return name + " by " + author.print();
    }
};

int main() {
    // Create Author objects
    Author author1("Mike", "..s@somewhere.com", 'm');
    Author author2("Alice", "..e@example.com", 'f');

    // Create Book objects
    Book book1("The Great Adventure", author1, 25.99);
    Book book2("Mystery in the Woods", author2, 19.99);

    // Display Book information using the print method
    cout << "Book 1: " << book1.print() << ", Price: $" << book1.getPrice() << endl;
    cout << "Book 2: " << book2.print() << ", Price: $" << book2.getPrice() << endl;

    // Test setters and getters
    author1.setEmail("author1@example.com");
    author2.setEmail("author2@example.com");
    book2.setPrice(29.99);

    // Display updated Book information
    cout << "After update:" << endl;
    cout << "Book 1: " << book1.print() << ", Price: $" << book1.getPrice() << endl;
    cout << "Book 2: " << book2.print() << ", Price: $" << book2.getPrice() << endl;

    return 0;
}