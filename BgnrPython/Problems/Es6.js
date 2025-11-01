const student = {
    name : "Amirhamza",
    age:34,
    address: {
        present: "uttora",
        parmanent:"mirpur"
    },
    grade: "A"
}
// console.log("HTis is main ",student);
// const grade: student.grade;
// destracturing 
const {grade:studentGrade,name:studentName,address:{present}}= student
// console.log(`This grade is:  ${studentGrade} and this name : ${studentName}`,present)


// defult vabe value set kora
// function moddhe diyao valu set korte pari


// function getStudent({name,address,grade}){
    // console.log(name,address,grade);
// }
// getStudent(student) 


// Araay 

const arry = [3,4,3,4,235,6,5,3,5,]
const [sencd, ,fourth , ...rest]=arry
console.log(sencd, fourth , ...rest);

// reduce
// acc amar kache joma :-0
// cur bortoman value array theke loop kore je ta asbe then cur amr sathe add hobe:-[array]
function sum (...num){
    // ...rest er kaj ami take ja dibo se tar array dibe
    console.log(num)
    return num.reduce((acc , cur)=> acc+cur,0 )
}
const result = sum(23,4,54,34,6,76,)
console.log(result);

const records = [
    {name:"amir",score:3,address:"Dhaka"},
    {name:"hamza",score:345,address:"rfh"},
    {name:"a;llskdj",score:456,address:"Dfghhaka"},
    {name:"nadiya",score:45,address:"hgfg"}
]
HightsPlayer = []
records.reduce((storeplyar,CurrentPlayar)=>{
    const highRuns = CurrentPlayar?.score>=100 ? "Top player":"LOw player"
    highRuns === "Top player" && HightsPlayer.push(CurrentPlayar)
    return HightsPlayer
    
},{})
const Topp = HightsPlayer.filter((plauer)=> plauer?.score>200)
console.log(Topp)
