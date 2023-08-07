#include "memberType.h"
#include <iostream>

// Default constructor
memberType::memberType() : personName(""), memberID(0), numBooksBought(0), totalAmountSpent(0.0) {}

// Parameterized constructor
memberType::memberType(const std::string& name, int memberID, int booksBought, double amountSpent)
    : personName(name), memberID(memberID), numBooksBought(booksBought), totalAmountSpent(amountSpent) {}

// Setter and Getter functions
void memberType::setName(const std::string& name) {
    personName = name;
}

std::string memberType::getName() const {
    return personName;
}

void memberType::setMemberID(int memberID) {
    this->memberID = memberID;
}

int memberType::getMemberID() const {
    return memberID;
}

void memberType::setBooksBought(int booksBought) {
    numBooksBought = booksBought;
}

int memberType::getBooksBought() const {
    return numBooksBought;
}

void memberType::setAmountSpent(double amountSpent) {
    totalAmountSpent = amountSpent;
}

double memberType::getAmountSpent() const {
    return totalAmountSpent;
}

// Member functions
void memberType::showPersonDetails() const {
    std::cout << "Name: " << personName << "\n";
    std::cout << "Member ID: " << memberID << "\n";
}

void memberType::showBooksAndAmountDetails() const {
    std::cout << "Books Bought: " << numBooksBought << "\n";
    std::cout << "Amount Spent: $" << totalAmountSpent << "\n";
}

bool memberType::isNameSimilar(const std::string& otherName) const {
    // Perform similarity check (you can define your own similarity criteria here)
    // For example, you can use string comparison functions like strcmp, etc.
    return personName == otherName;
}
