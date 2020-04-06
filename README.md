# Text-Sequence-Manipulation

### Question 1 - Spammer

You work for SPAM Marketing Co. Your supervisor has just received a text file (MonsterJobsData_variations.txt – a UTF-8 encoded file) containing, what she believes, will be pure SPAM marketing gold - previously un-spammed email addresses.

You have been asked to author a Python script and the necessary regular expressions to extract all of the email addresses from that file.Since HTTP is case insensitive, your RE patterns should be case insensitive.

Input Files Used: MonsterJobsData_variations.txt – a UTF-8 encoded file

### Requirements Overview
1. open the file for reading
2. for each line in the file, use a RE to scan and capture the line for URLs.
3. Output the captured email addresses.

### Additional Information
Obscured Email Addresses
Regarding emails, alas, some folks are wise to your “spammer” tactics and obscure their email addresses in cleaver ways. Specifically, you are to recognize and retain emails of the following form:

a. a valid email address format (see below)
<br> b. robertsj1503 at duq dot edu
<br> c. robertsj1503_at_duq_dot_ edu
<br> d. jeff dot Roberts at duq dot edu
<br> e. Email Address with plenty of HTML comment tags! <!-- -->robertsj1503<!-- -->@<!-- -->duq<!-- -->.edu<!-- -->


Valid Email Addresses
The local-part of a valid email address (the part before the @) may use any of these ASCII characters:
1. uppercase and lowercase latin letters A to Z and a to z
2. digits 0 to 9
3. printable characters !#$%&'*+-/=?^_`{|}~.

<br>The domain-part of a valid email address (the part after the @) may only contain: uppercase and lowercase ASCII letters A to Z and a to z , digits 0 to 9 , hyphen - provided that it is not the first or last character

### Output
Write the list of email addresses (one email per line) to a text file named found_emails.txt. Do not change or otherwise re-interpret the non-standard emails into RFC 5322 compliant email addresses. Just output the emails as you found them. (Ex: robertsj1503 at duq dot edu).

---------------------------------------------------------------------------------------------------------------------------------------

### Question 2 – Poor-Man’s Sentiment Analysis (Part 1)

Use Yelp’s GraphQL API to return 50 dentists in the in the “Downtown, Pittsburgh, PA” location. Once found, order the list of dentists according to their ratings.

Script Name Requirement: yelp_sent_analysis_p1.py

### Requirements Overview
1. Your initial search should search for and return 50 Dentists in the “Downtown, Pittsburgh, PA” location
2. Your search query must request the results by sorted by the best_match criterion
3. Your GraphQL search query need only request a business object’s name, rating, and id attributes
4. Sort the returned list of dentists in descending order according to their Yelp ratings. Any ratings ties can be ignored.
5. Output the captured business information.

### Output
Write your ordered lists of dentists to yelp_dentists.csv using a CSV file format (one dentist per line).

---------------------------------------------------------------------------------------------------------------------------------------

### Question 3 – Poor-Man’s Sentiment Analysis (Part 2)

In this question you will use the yelp_dentists.csv file created in the previous question to conduct a bag-of-words sentiment analysis.

Script Name Requirement: yelp_sent_analysis_p2.py

### Input Files Used:
<br> yelp_dentists.csv – UTF-8 encoded csv file
<br> positive_words.txt – ANSI encoded text file
<br> negative_words.txt – ANSI encoded text file

### Requirements Overview
1. Ingest the positive words into a single list
2. Ingest the negative words into a single list
3. open the csv file for reading
4. parse the opened file using the csv module
5. for each business, use Yelp’s GraphQL reviews query API to return the business’ review text
6. For each business, record the (a) count of positive words and (b) count of negative words occurring across all reviews
7. Output your results

### Output
Print your results as follows (replace the bracketed items using your results):

‘The reviews for Business Id: <id>, Business Name: <name> contained the most positive words with <xxx> positive words.’
  
‘The reviews for Business Id: <id>, Business Name: <name> contained the most negative words with <xxx> negative words.’
  
 --------------------------------------------------------------------------------------------------------------------------------------
 
 ### Question 4 – The latin Pig Cipher
 
It turns out Julius Caesar was more paranoid than first thought. He had another cipher which was a combination of Pig Latin and step cipher. You are tasked with implementing the so-called Latin Pig Cipher (LPC). You may use any combination of RE or string operations you wish in constructing your solution.

The latin_pig_cipher function receives a (word/string) and a step value as parameters. The objective of the function is to convert an incoming string to its LPC equivalent and return the result.

Script Name Requirement: latin_pig_cipher.py.

### Requirements Overview

1. A word is a consecutive sequence of letters (a-z, A-Z) and numeric digits (0-9). You may assume that the string input to the function will only be a single "word". Examples: Zebra29, apple85, etc.
2. A cipher shifted letter is substitution cipher in which the letter in the plaintext is replaced by a letter some fixed number of step positions down the alphabet. For example, with a step of 2, D would be replaced by F, E would become G. Numeric digits are not cipher shifted.
3. If word ends with a digit, or a series of consecutive digits, the minimum digit in the series becomes the cipher step value. Thus, overriding (replacing) the step input parameter. Note: a series composed of a single digit has a minimum value equal to that digit.
4. If a word starts with a vowel, the LPC version is the original word with the string ŵāŷ (latin small letter W with circumflex (Unicode code point \x0175) + latin small letter A with macron (Unicode code point \x0101) + latin small letter Y with circumflex (Unicode code point \x0177)) to the end.
5. If the first letter of a word is the letter 'y', the 'y' should be treated as a consonant, unless it is followed by a numeric digit. If the first letter of a word is a 'y' followed by a digit, it is to treated as a vowel as are any other occurrences of 'y'.
6. If a word starts with a consonant, or a series of consecutive consonants, the LPC version transfers ALL cipher shifted consonants up to the first vowel to the end of the word, and adds the string "āŷ" (latin small letter A with macron (Unicode code point \x0101) + latin small letter Y with circumflex (Unicode code point \x0177) to the end.
7. If the original word was capitalized, the new LPC version of the word should also be capitalized in the first letter. If the original capital letter was a consonant, and thus moved, it should no longer be capitalized in its new location.

Print the results of your algorithm against the test data.

Test Word (keys)           --          Pig latin (values)
<br> football415           --             ootball415gāŷ
<br> Pittsburgh            --               Ittsburghpāŷ
<br> Y2ellow               --               Y2ellowŵāŷ
<br> yellow                --               ellowyāŷ
<br> yttrium               --             iumyttrāŷ
