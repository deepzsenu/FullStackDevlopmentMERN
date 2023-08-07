#include "memberType.h"
#include <iostream>

int main() {
    // Creating memberType objects
    memberType member1("John Doe", 1001, 5, 75.50);
    memberType member2("Jane Smith", 1002, 3, 45.25);

    // Showing person details
    std::cout << "Member 1:\n";
    member1.showPersonDetails();

    std::cout << "\nMember 2:\n";
    member2.showPersonDetails();

    // Checking name similarity
    std::string nameToCheck = "John Doe";
    if (member1.isNameSimilar(nameToCheck)) {
        std::cout << "\nName similarity found with Member 1\n";
    } else {
        std::cout << "\nName similarity not found with Member 1\n";
    }

    // Updating books bought and amount spent for Member 2
    member2.setBooksBought(6);
    member2.setAmountSpent(56.75);

    // Showing updated books and amount details for Member 2
    std::cout << "\nUpdated Details for Member 2:\n";
    member2.showBooksAndAmountDetails();

    return 0;
}
