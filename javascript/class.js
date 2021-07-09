let rect = class Rectangle {
    constructor(height, width) {
            this.height = height;
            this.width = width;
        }
        //getter
    get area() {
        return this.calArea();
    }

    calArea() {
        return this.height * this.width
    }
}

const square = new rect(20, 20)
console.log(rect.calArea)

let students = class ClassRoom {
    constructor(...name) {
        this.name = name;
    }

    get names() { return this.name }
}

const student = new students("becky", "ronah", "julie");
console.log(student.name)


let creature = class Animals {
    constructor(name, sound, move) {
        this.name = name;
        this.sound = sound;
        this.move = move;
    }

    get bark() { return this.sound }


    static movement(a, b) {
        return "The " + a + " " + b;
    }

}

const dog = new creature("dog", "barks", "runs")

console.log(dog.movement)
console.log(dog.bark)
console.log(creature.movement("man", "speaks"))

var name1 = "MiloYulinapoilus";
res = name1.slice(3, 7);
console.log(res);

let numbers = [4, 25, 64];
let square_of = numbers.map(function(x) { return Math.sqrt(x) })
let gth = numbers.filter(x => { x > 10; return x > 10 });
console.log(square_of);
console.log(gth);