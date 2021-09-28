import {User} from "./User"

function main(){
    let manny = new User(22, "Manny", 420);
    let annabelle = new User(24, "Annabelle", 69)
    manny.info();
    annabelle.info();
} //end main
main();