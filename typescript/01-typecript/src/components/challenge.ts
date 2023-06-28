 export const solution=(number: number) =>{
        let sum : number[]=[];

        if(number <= 0 ){
            return 0
        }else{
            for(let i = 1 ; i < number ; i ++){
                if(i % 3 === 0 || i % 5 === 0  ){
                    if(!sum.includes(i)){
                        sum.push(i)
                    }
                }
            }
            return sum.reduce((prevValue, currentValue) =>  prevValue + currentValue )
        }

    }
 console.log(solution(10));