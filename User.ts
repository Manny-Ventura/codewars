export class User {
    age: number; 
    name: string;
    musicScore: number;
    color: "pink";
    sex: true;

    constructor(x: number, y: string, z: number) {
        this.age = x;
        this.name = y;
        this.musicScore = z;
    } //end constructor
    //new function
    info(){
        console.log("Wassup " + this.name + ", heres your info and shit: \n");
        console.log("Your age: " + this.age + "\n");
        console.log("Your name: " + this.name + "but i already told you retard\n");
        console.log("your grade in english class: " + this.musicScore + "\n")
    } //end of info

    scorePlusOne(){
        console.log(`original score: ${this.musicScore}\n`);
        this.musicScore++;
        console.log(`new score: ${this.musicScore}`);
    } //end scorePlusOne
    sexyInfo(){
        console.log("I am sexy: " + this.sex);
    } //end sexyInfo 
} //end User class