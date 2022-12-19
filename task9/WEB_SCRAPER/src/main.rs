
extern crate reqwest;
extern crate scraper;


use csv::Writer;

fn main() {

    let response = reqwest::blocking::get(
        "https://crypto.com/price",)
        .unwrap()
        .text()
        .unwrap();

    let document = scraper::Html::parse_document(&response);

    let title_names = scraper::Selector::parse("div.css-ttxvk0>p").unwrap();
    let _titles = document.select(&title_names).map(|x| x.inner_html());
    
    let title_change = scraper::Selector::parse("div.css-16q9pr7>p").unwrap();
    let _change = document.select(&title_change).map(|x| x.inner_html());
    
    let title_price = scraper::Selector::parse("div.css-b1ilzc").unwrap();
    let _price = document.select(&title_price).map(|x| x.inner_html());

    let title_vol = scraper::Selector::parse("td.css-1nh9lk8").unwrap();
    let _vol = document.select(&title_vol).map(|x| x.inner_html());
    
    //Have Run it just for checking
    // titles.zip(1..51)
    // .for_each(|(title, i)| {println!("{}: {}", i, title);});
    // prices.zip(1..51)
    // .for_each(|(price, i)| {println!("{}: {}", i, price);});
    // costs.zip(1..51)
    // .for_each(|(cost, i)| {println!("{}: {}", i, cost);});
    // vol.zip(1..51)
    // .for_each(|(cost, i)| {println!("{}: {}", i, cost);});

    //For Storing the information extracted from the documents
    let mut titles = document.select(&title_names);
    let mut change = document.select(&title_change);
    let mut price = document.select(&title_price);
    let mut vol = document.select(&title_vol);
    


    /*
    Mutable writer pointed towards to foo.csv
    */
    let mut wtr = Writer::from_path("foo.csv").unwrap();

    //Used to write in csv file these are table headers
    wtr.write_record(&["Name","Price","24H Change","24H Volume"]).expect("cannot write");


    //Running the loop 50 times to get the top 50 Crypto 
    for _i in 1..51{
        
        let name = titles.next().unwrap().text().collect::<String>();
        
        let price = price.next().unwrap().text().collect::<String>();
        
        let h24ch = change.next().unwrap().text().collect::<String>();
        
        let h24vol = vol.next().unwrap().text().collect::<String>();
        
        wtr.write_record([name,price,h24ch,h24vol]).expect("cannot write");
    }
    
}
    

