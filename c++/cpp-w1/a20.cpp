#include <iostream>
#include <string>
#include <memory>



class Car : public std::enable_shared_from_this<Car> {
	public:
		std::string maker;
		std::string model;

	Car(std::string maker1, std::string model1) : maker(maker1) , model(model1) {
		
	}

	void get_info() {
		std::cout << maker << " " << model << std::endl;
	}

	std::shared_ptr<Car> getShared() {
		return shared_from_this();
	}
};

int main() {
	std::string maker = "mazda";
	std::string model = "rx7";
	std::shared_ptr<Car> p1 = std::make_shared<Car>(maker, model);
	std::shared_ptr<Car> p3 = p1->getShared();

	std::shared_ptr<Car> p2 = std::move(p1);
	p2->get_info();		
	p3->get_info();		

	
}
