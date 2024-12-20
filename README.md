
# anime-facts-rest-api 🐱‍🚀

An API in Pure Python that will return anime facts. 
Inspired by [Check](https://chandan-02.github.io/anime-facts-rest-api/) but write in pure python

# Usage :

  > Note: This project is can be hosted on Koeyb with free account;

# Warning :

http.server is not recommended for production. It only implements basic security checks. 
So if you think scale this use appropriate methods to protect the API instead expose directly to internet

### Home Route
Get all the available anime's list : `http://localhost:8080/api/v1`
*returns* : 
```
{
	success:true,
	data: [
		{
			anime_id: 1,
			anime_name: "bleach",
			anime_img: "https://exampleimage.com/"
		},
		{
			anime_id: 2,
			anime_name: "black_clover",
			anime_img: "https://exampleimage2.com/"
		},
		...
	]
}
```
### Anime Facts Route 
Get all facts related to an Anime  : `http://localhost:8080/api/v1/?q=:anime_name`
> Provide an anime name (from the available option) in place of `:anime_name`

***Example*** : 
`http://localhost:8080/api/v1/?q=fma_brotherhood`
*returns* : 
```
{
	success:true,
	total_facts: 8,
	anime_img:"https://exampleimage.com/",
	data: [
		{
			fact_id: 1,
			fact: "Ishvalans And Ametris Conflict Is Based On Hokkaido s Ainu People"
		},
		{
			fact_id: 2,
			fact: "Arakawa Actually Bought Military Prop Guns For Drawing References"
		},
		...
	]
}	
```
### Specific Fact Route 
Get all facts related to an Anime  : `http://localhost:8080/api/v1/?q=:anime_name&i=:fact_id`
> Provide an anime name & fact id (from the available option) in place of `:anime_name & :fact_id`

***Example*** : 
`http://localhost:8080/api/v1/?q=fma_brotherhood&i=2`
*returns* : 
```
{
	success:true,
	data: {
			fact_id: 2,
			fact: "Arakawa Actually Bought Military Prop Guns For Drawing References"
	}
	
}
```

- Clone the repo : `git clone https://github.com/xslackx/anime-facts-rest-api.git`

- Run : `cd anime-facts-rest-api && chmod u+x app.py` & `./app.py`

