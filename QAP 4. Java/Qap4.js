const customer = {
    firstName: "Donovan",
    lastName: "Head",
    bday: new Date(2001,9,13),
    gender: "Male",
    phoneNum: "(709)424-6930",
    mailAddr: {
        streetAdd: "41 wings point road",
        city: "spaniards bay",
        postal: "A0A 3X0",
        province: "Newfoundland and Labrador",
        country: "Canada"
    },
    roomPref: ["Non-Smoking", "King-Size Bed", "Ocean View"],
    payMethod: "Visa",
    checkDates: {
        checkIn: new Date (2024,4,10),
        checkOut: new Date (2024,4,15),
    },
    secAnswer: "Ruckus",
    reservationNum: "1234567890",
    servedBy : "John Doe",
    valet : "Yes",
    age: function() {
        let birthYear = this.bday.getFullYear();
        let today = new Date();
        let todayYear = today.getFullYear();
        let age = todayYear - birthYear;
        return age;
    },

    durationofstay: function() {
        let durationMs = this.checkDates.checkOut - this.checkDates.checkIn
        let dayMS = (1000*60*60*24)
        let durationDays = (durationMs/dayMS)
        return durationDays
    },
    checkinformat: function() {
        let checkInfor = this.checkDates.checkIn.toISOString().slice(0,10)
        return checkInfor
    },
    checkoutformat: function() {
        let checkOutFor = this.checkDates.checkOut.toISOString().slice(0,10)
        return checkOutFor
    },
    bdayformat: function(){
        let bdayfor = this.bday.toISOString().slice(0,10)
        return bdayfor
    }
}

let Para = `Employee ${customer.servedBy} checked in ${customer.firstName} ${customer.lastName}, ${customer.gender}, who will be staying at the Motel for ${customer.durationofstay()} days, arriving on ${customer.checkinformat()} and will be staying until ${customer.checkoutformat()} under reservation number ${customer.reservationNum}. ${customer.firstName} ${customer.lastName} can be reached at ${customer.phoneNum} or via mail. Mailing adrress is as follows: ${customer.mailAddr.streetAdd}, ${customer.mailAddr.city} ${customer.mailAddr.postal}, ${customer.mailAddr.province}, ${customer.mailAddr.country}. ${customer.lastName} is ${customer.age()} years old, born ${customer.bdayformat()}. He prefers rooms ${customer.roomPref}, answered ${customer.valet} to valet service, and will be paying ${customer.payMethod}. Security question to access his reservation is "What is your cats name" and ${customer.lastName}'s answer is "${customer.secAnswer}".`


console.log(Para)

document.body.innerHTML = Para


