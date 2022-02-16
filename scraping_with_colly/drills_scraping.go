package main

import (
	"github.com/gocolly/colly"
	"encoding/csv"
	"fmt"
	"strconv"
	"os"
	"log"
	"strings"
	"time"
)


func main () {
	start := time.Now()

    file_name:= "drills.csv"
    file, err := os.Create(file_name)
    if err != nil {
		log.Fatalf("could not create the file, err :%q",err)
		return
    }

	defer file.Close()

	writer := csv.NewWriter(file)
	writer.Write(
		[]string {
			"url",
			"title",
			"brand",
			"current_price",
			"average_rating",
			"number_of_ratings",
		},
	)
	defer writer.Flush()

	collector := colly.NewCollector(
        colly.AllowedDomains("manomano.fr", "www.manomano.fr"),
    )

	collector.OnHTML(".root_6be42578", func(element *colly.HTMLElement){
		var url, title, brand, price_integer, price_decimal, average_rating, number_of_ratings string

		content_container := "div.contentContainer_6be42578"
		price_container := content_container + " > div[data-testid=detailed-price] > span[data-testid=price-main]"
		ratings_container := content_container + " > div.ratingsContainer_0bd478b7 > div"

		title_class := content_container + " > div.title_6be42578"
		brand_class := "div.visualDetails_6be42578 > div[role=contentinfo] > img"


		url = element.Attr("href")
		title = element.ChildText(title_class)
		brand = element.ChildAttr(brand_class, "alt")
		brand = strings.Trim(brand, "brand image of \"")

		price_integer = element.ChildText(price_container + " > span.integer_fb1cf7b2")
		price_decimal = element.ChildText(price_container + " > sup > span.decimal_fb1cf7b2")
		average_rating = element.ChildAttr(ratings_container + " > span", "aria-label")
		number_of_ratings = element.ChildText(ratings_container + " > div")

		current_price := price_integer

		if price_decimal != "" {
			current_price = current_price + "." + price_decimal
		}



		if average_rating != "" {
			average_rating = strings.Trim(average_rating, "/5")
		}

		writer.Write(
			[]string {
				url,
				title,
				brand,
				current_price,
				average_rating,
				number_of_ratings,
			},
		)
	})

	for i:=1; i<=3; i++ {

		fmt.Printf("Scraping Page : %d\n",i)
		collector.Visit("https://www.manomano.fr/perceuse-1146?page="+strconv.Itoa(i))

	}
	log.Printf("Scraping Complete\n")
	log.Println(collector)

	elapsed := time.Since(start)
    log.Printf("Scraping took %s", elapsed)
}