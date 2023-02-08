#pragma once
#include "../ClassA/ClassA.hpp"

/*!
* \brief This Enum contains some IDs for ClassB
*/
enum class B_ID
{
    value_one,
    value_two    
};

/*
* This class contains some more advanced members.
*/
class ClassB
{
private:
    ClassA member_1; /* stores a ClassA instance*/

public:
    B_ID id = B_ID::value_one; /* stores a B_ID*/

    /*!
    * \brief Basic Constructor
    */
    ClassB();
};