main_js = """
    const days = arguments[0];
    const city_selector = arguments[1];
    const city_name = arguments[2].charAt(0).toUpperCase()+arguments[2].slice(1)
    const link = arguments[3];
    const date = arguments[4];
    function days_checker(string){
        day = ""
        if(string.includes("godz") || string.includes("min")){
            day = 1
        }
        else{
            for(let x of string){
                if(isNaN(x) == false){
                    day += x
                }
                else{
                    break
                }
            }
        }
        return parseInt(day)
    }
    
    function justJoinScraper(){
        const date_posted = link.querySelector(date).innerText
        const city = link.querySelector(city_selector).innerText
        if(String(city).includes(city_name.slice(0,3))){
            if(String(date_posted).includes("New") != true){
                const days_ago = days_checker(date_posted)
                console.log(days_ago)
                if(days_ago > days){
                    return false
                }
            }
        }
    }
    return justJoinScraper()
"""
scroll_js = """
    const bar = arguments[0];
    const timer = arguments[1];
    const main_link = arguments[2];
    const scroll_bar = document.querySelector(bar).scroll(0,timer)
    if(main_link.includes("linkedin")){
        if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight){
            return "bottom"
        }
    }
"""
