

#include <iostream>
#include <ctime>

using namespace std;

class ATM
{
private:
    int pin;
    double balance;
    time_t currentTime;

public:
    ATM();
    void welcome();
    void displayDateTime();
    void login();
    void showMenu();
    void checkBalance();
    void deposit();
    void withdraw();
    void exit();
};

ATM::ATM()
{
    pin = 12345;
    balance = 0.0;
}

void ATM::welcome()

{
    char welcome;
    cout << "\n********** WELCOME TO ATM **********\n\n-------------------------------------\n"<< welcome << endl;
} 



void ATM::displayDateTime()
{   char a;
    currentTime = time(nullptr);
    cout << "Current Date and Time: " << ctime(&currentTime) << endl; 
    cout << "------------------------------------- \n" << a << endl;
}

void ATM::login()
{
    int enteredPin;
    cout << "Enter your Account pin Access Number ![Only One Attempt is allowed]: ";
    cin >> enteredPin;
    if (enteredPin == pin)
    {
        showMenu();
    }
    else
    {
        cout << "Invalid PIN. You had made your attempt which failed !!! No more attempts allowed !! Sorry!! " << endl;
    }
}

void ATM::showMenu()
{
    int choice;
    do
    {
        cout << "\n************ ATM Main Menu Screen ************\n" << endl;
        cout << "Enter [1] To Check Balance" << endl;
        cout << "Enter [2] To Deposit" << endl;
        cout << "Enter [3] To Withdraw" << endl;
        cout << "Enter [0] To Exit ATM\n" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            checkBalance();
            break;
        case 2:
            deposit();
            break;
        case 3:
            withdraw();
            break;
        case 0:
            exit();
            break;
        default:
            cout << "Invalid choice. Please try again." << endl;
        }
    } while (choice != 4);
}

void ATM::checkBalance()
{
    cout << "Your Current Balance: $" << balance << endl;
}

void ATM::deposit()
{
    double amount;
    cout << "Enter the amount to deposit: $";
    cin >> amount;
    if (amount > 0)
    {
        balance += amount;
        cout << "Deposit successful. Current Balance: $" << balance << endl;
    }
    else
    {
        cout << "Invalid amount. Please try again." << endl;
    }
}

void ATM::withdraw()
{
    double amount;
    cout << "Enter the amount to withdraw: $";
    cin >> amount;
    if (amount > 0)
    {
        if (amount <= balance)
        {
            balance -= amount;
            cout << "Withdrawal successful. Current Balance: $" << balance << endl;
        }
        else
        {
            cout << "Insufficient balance. Please try again." << endl;
        }
    }
    else
    {
        cout << "Invalid amount. Please try again." << endl;
    }
}

void ATM::exit()
{
    cout << "Thank you for using the ATM !" << endl;
    // Add any necessary cleanup or additional exit logic here.
}

int main()
{
    ATM atm;
    atm.welcome();
    atm.displayDateTime();
    atm.login();

    return 0;
}
