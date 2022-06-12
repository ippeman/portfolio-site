taskSubmit.addEventListener("click",() =>{
    let taskValue = document.getElementById("taskValue");
    let taskSubmit = document.getElementById("taskSubmit");
    let li = document.createElement("li");
    let ul = document.getElementById("taskList");
    let text = document.createTextNode(taskValue.value);
    li.appendChild(text);
    ul.appendChild(li);
})

let table = document.getElementById("skill_group2");
let skill = ["HTML","CSS", "python","mysql", "postgreSQL", "C言語"];
let efficiency = ["★★★","★★★","★★★","★★★","★★★","★★★"];

for(let i=0;i<skill.length;i++){
    let tr = document.createElement("tr");
    let td = document.createElement("td");
    let text2 = document.createTextNode(skill[i]);
    let td2 = document.createElement("td");
    let text3 = document.createTextNode(efficiency[i]);    
    td.appendChild(text2);
    td2.appendChild(text3);
    tr.appendChild(td);
    tr.appendChild(td2);
    table.append(tr);
    table.style.textAlign="center";
}

window.onload = function(){
    let today = new Date();
    let year = today.getFullYear();
    let month = today.getMonth()+1;
    let date = today.getDate();
    let hours = today.getHours();
    let minutes = today.getMinutes();
    let seconds = today.getSeconds();
    today = year+"年"+month+"月"+date+"日"+hours+"時"+minutes+"分"+seconds+"秒";
    let text4 = document.createTextNode(today);
    let one = document.getElementById("date");
    one.appendChild(text4);

    let myBirth = document.getElementById("myAge");
    let myAge = year - 1999;
    if (month < 9){
        myAge--;
    }else if(month == 9 && date < 26){
        myAge--;
    }                                                   
    let text5 = document.createTextNode(myAge);
    myBirth.appendChild(text5);
}

