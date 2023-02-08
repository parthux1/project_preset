#pragma once

/*!
* \brief ClassA is used as an documentation example
*/
class ClassA
{
private:
	int member_1 = 1; /*! This is a private member*/

public:
	int member_2 = 2; /*! This is a public member*/

	/*!
	* \brief this functions does nothing
	* \param parameter_1 first parameter
	* \param parameter_2 second parameter, defaults to 'a'
	*/
	void foo(unsigned int parameter_1, char parameter_2='a') const noexcept;
};