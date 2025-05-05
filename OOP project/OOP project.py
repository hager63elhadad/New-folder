class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate 

    def sleep(self, hours):
        if hours == 7:
            self.mood = "active"
        elif hours < 7:
            self.mood = "average"
        else:
            self.mood = "tired"

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50
        else:
            self.healthRate = max(0, self.healthRate - 25)  

    def buy(self, items):
        cost = items * 10
        if self.money >= cost:
            self.money -= cost
        else:
            print("Not enough money to buy items.")


class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self._fuelRate = 100 if fuelRate > 100 else max(0, fuelRate)
        self._velocity = velocity if 0 <= velocity <= 200 else 0

    @property
    def fuelRate(self):
        return self._fuelRate

    @fuelRate.setter
    def fuelRate(self, value):
        self._fuelRate = min(100, max(0, value))

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if 0 <= value <= 200:
            self._velocity = value
        else:
            print("Velocity must be between 0 and 200.")

    def run(self, distance, velocity):
        self.velocity = velocity
        print(f"[Car] Starting to drive at {self.velocity} km/h for {distance} km.")

        fuel_needed = (distance // 10) * 10
        if fuel_needed > self.fuelRate:
            max_distance = (self.fuelRate // 10) * 10
            self.fuelRate = 0
            self.stop(distance - max_distance)
        else:
            self.fuelRate -= fuel_needed
            self.stop(0)

    def stop(self, remaining_distance):
        self.velocity = 0
        if remaining_distance > 0:
            print(f"[Car] Stopped before arriving. {remaining_distance} km remaining.")
        else:
            print("[Car] Arrived at destination and stopped.")


class Employee(Person):
    def __init__(self, name, money, mood, healthRate, emp_id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, distance, velocity):
        print(f"[Employee] {self.name} is driving to work...")
        self.car.run(distance, velocity)

    def refuel(self, gasAmount=100):
        print(f"[Employee] {self.name} is refueling the car with {gasAmount}%.")
        self.car.fuelRate += gasAmount

    def send_mail(self, to, subject, body):
        print(f"Sending email to {to}\nSubject: {subject}\n{body}")


class Office:
    employeesNum = 0  

    def __init__(self, name):
        self.name = name
        self.employees = []  

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1
        print(f"[Office] Hired {employee.name}")

    def fire(self, empId):
        before_count = len(self.employees)
        self.employees = [emp for emp in self.employees if emp.id != empId]
        if len(self.employees) < before_count:
            Office.employeesNum -= 1
            print(f"[Office] Fired employee with ID {empId}")

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp:
            emp.salary -= deduction
            print(f"[Office] Deducted {deduction} from {emp.name}. New salary: {emp.salary}")

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp:
            emp.salary += reward
            print(f"[Office] Rewarded {reward} to {emp.name}. New salary: {emp.salary}")

    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if not emp:
            print("[Office] Employee not found.")
            return

        is_late = Office.calculate_lateness(9.0, moveHour, emp.distanceToWork, emp.car.velocity)
        if is_late:
            self.deduct(emp.id, 10)
        else:
            self.reward(emp.id, 10)

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        if velocity == 0:
            return True
        arrival_time = moveHour + (distance / velocity)
        return arrival_time > targetHour

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num


if __name__ == "__main__":
   
    samy_car = Car(name="Fiat 128", fuelRate=80, velocity=60)

    samy = Employee( name="Samy",  money=500,  mood="neutral", healthRate=100, emp_id=1, car=samy_car, email="samy@iti.org", salary=3000,
        distanceToWork=20 )


    iti_office = Office("ITI Smart Village")
    iti_office.hire(samy)

   

