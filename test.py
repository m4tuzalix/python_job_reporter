justJoinIt = """
    function justJoinScraper(){
        var taken = []
        var scroll_value = 700
        const loop = setInterval(()=>{
            var e = document.querySelectorAll("a.css-18rtd1e")
            for(let x=0;x<e.length;x++){
                const link = "https://justjoin.it"+e[x].getAttribute("href")
                var date_posted = e[x].querySelector("div.css-v6uxww div").innerText
                const city = document.querySelector("div.css-1ihx907").innerText
                if(city == "Wrocław"){
                    if(String(date_posted).includes("New") != true){
                        const days_ago = String(date_posted).split("d")
                        if(parseInt(days_ago[0]) < 6){
                            double_check(link)
                        }
                        else{
                            clearInterval(loop)
                        }
                    }
                    else{
                        double_check(link)
                    }
                }
            }
            var bar_scroll = document.querySelector("div.css-1macblb")
            bar_scroll.scroll(0,scroll_value)
            scroll_value += 700
        },1)
        function double_check(value){
            const given_link = taken.indexOf(value)
            if(given_link === -1){
                taken.push(value)
            }
        }
        console.log(taken)
    }
    justJoinScraper()
    return taken
"""
test = """
    const timer_value = arguments[0];
    const days = arguments[1];
    function justJoinScraper(){
        var e = document.querySelectorAll("a.css-18rtd1e")
        for(let x=0;x<e.length;x++){
            const link = "https://justjoin.it"+e[x].getAttribute("href")
            var date_posted = e[x].querySelector("div.css-v6uxww div").innerText
            const city = document.querySelector("div.css-1ihx907").innerText
            if(city == "Wrocław"){
                if(String(date_posted).includes("New") != true){
                    const days_ago = String(date_posted).split("d")
                    if(parseInt(days_ago[0]) > days){
                        return false
                    }
                }
            }
        }
        var bar_scroll = document.querySelector("div.css-1macblb").scroll(0,timer_value)
        return true
    }
    return justJoinScraper()
"""