#ifndef MEMBERTYPE_H
#define MEMBERTYPE_H

#include <string>

class memberType {
public:
    memberType(); // Default constructor
    memberType(const std::string& name, int memberID, int booksBought, double amountSpent); // Parameterized constructor

    // Member functions
    void setName(const std::string& name);
    std::string getName() const;

    void setMemberID(int memberID);
    int getMemberID() const;

    void setBooksBought(int booksBought);
    int getBooksBought() const;

    void setAmountSpent(double amountSpent);
    double getAmountSpent() const;

    void showPersonDetails() const;
    void showBooksAndAmountDetails() const;
    bool isNameSimilar(const std::string& otherName) const;

private:
    std::string personName;
    int memberID;
    int numBooksBought;
    double totalAmountSpent;
};

#endif // MEMBERTYPE_H
