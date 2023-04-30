import openai
import os


from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


# Guideline: Provide specific instructions

# code = f"""
# it should allow the user to enter his birthday date on an input \
# and after he press a submit button, he receives a different \
# celebration message on the bottom of the page on a h2 tag.

# all elements should be centered. Use flexbox for this.
# """

# prompt= f"""
# Create a Angular functional component according to the following \
# guidelines: 
# ```{code}```
# """

# Guideline: Give time to think

# prompt = f"""
# Determine if the student's solution is correct:

# Question:
# Imagine I have create a new imaginary polygonal figure called Mouse. \
# To calculate its imaginary area, we should do the following: \
# - Multiply its width times 3 \
# - Later, sum its height to the previous result\
# We will calculate just the value of the area.  

# What is the area of a new "Mouse" figure that \
# has 40 as width and 50 as height?

# Student's Solution:
# Let x be the area of the "Mouse" figure.
# - area = width*3 + height
# Area of the Mouse figure is: 50*3 + 40 = 170
# """



# Guideline: Iterative - Change the focus of the output. It is helpful for marketing
# fact_sheet_chair = """
# OVERVIEW
# - Part of a beautiful family of mid-century inspired office furniture, 
# including filing cabinets, desks, bookcases, meeting tables, and more.
# - Several options of shell color and base finishes.
# - Available with plastic back and front upholstery (SWC-100) 
# or full upholstery (SWC-110) in 10 fabric and 6 leather options.
# - Base finish options are: stainless steel, matte black, 
# gloss white, or chrome.
# - Chair is available with or without armrests.
# - Suitable for home or business settings.
# - Qualified for contract use.

# CONSTRUCTION
# - 5-wheel plastic coated aluminum base.
# - Pneumatic chair adjust for easy raise/lower action.

# DIMENSIONS
# - WIDTH 53 CM | 20.87”
# - DEPTH 51 CM | 20.08”
# - HEIGHT 80 CM | 31.50”
# - SEAT HEIGHT 44 CM | 17.32”
# - SEAT DEPTH 41 CM | 16.14”

# OPTIONS
# - Soft or hard-floor caster options.
# - Two choices of seat foam densities: 
#  medium (1.8 lb/ft3) or high (2.8 lb/ft3)
# - Armless or 8 position PU armrests 

# MATERIALS
# SHELL BASE GLIDER
# - Cast Aluminum with modified nylon PA6/PA66 coating.
# - Shell thickness: 10 mm.
# SEAT
# - HD36 foam

# COUNTRY OF ORIGIN
# - Italy
# """

# prompt = f"""
# Your task is to help a marketing team create a 
# description for a retail website of a product based 
# on a technical fact sheet.

# Write a product description based on the information 
# provided in the technical specifications delimited by 
# triple backticks.

# Technical specifications: ```{fact_sheet_chair}```
# """

# prompt = f"""
# Your task is to help a marketing team create a 
# description for a retail website of a product based 
# on a technical fact sheet.

# Write a product description based on the information 
# provided in the technical specifications delimited by 
# triple backticks.

# Use at most 100 words
# Technical specifications: ```{fact_sheet_chair}```
# """

# prompt = f"""
# Your task is to help a marketing team create a 
# description for a retail website of a product based 
# on a technical fact sheet.

# Write a product description based on the information 
# provided in the technical specifications delimited by 
# triple backticks.

# Use at most 2 sentences
# Technical specifications: ```{fact_sheet_chair}```
# """

# prompt = f"""
# Your task is to help a marketing team create a 
# description for a retail website of a product based 
# on a technical fact sheet.

# Write a product description based on the information 
# provided in the technical specifications delimited by 
# triple backticks.

# Use at most 250 characters
# Technical specifications: ```{fact_sheet_chair}```
# """

# prompt = f"""
# Your task is to help a marketing team create a 
# description for a retail website of a product based 
# on a technical fact sheet.

# Write a product description based on the information 
# provided in the technical specifications delimited by 
# triple backticks.

# The description is intended for furniture retailers, 
# so should be technical in nature and focus on the 
# materials the product is constructed from.

# Use at most 50 words
# Technical specifications: ```{fact_sheet_chair}```
# """

# prompt = f"""
# Your task is to help a marketing team create a 
# description for a retail website of a product based 
# on a technical fact sheet.

# Write a product description based on the information 
# provided in the technical specifications delimited by 
# triple backticks.

# The description is intended for furniture retailers, 
# so should be technical in nature and focus on the 
# materials the product is constructed from.

# At the end of the description, include every 7-character 
# Product ID in the technical specification.

# Use at most 50 words
# Technical specifications: ```{fact_sheet_chair}```
# """

# prompt = f"""
# Your task is to help a marketing team create a 
# description for a retail website of a product based 
# on a technical fact sheet.

# Write a product description based on the information 
# provided in the technical specifications delimited by 
# triple backticks.

# The description is intended for furniture retailers, 
# so should be technical in nature and focus on the 
# materials the product is constructed from.

# At the end of the description, include every 7-character 
# Product ID in the technical specification.

# After the description, include a table that gives the 
# product's dimensions. The table should have two columns.
# In the first column include the name of the dimension. 
# In the second column include the measurements in inches only.

# Give the table the title 'Product Dimensions'.

# Format everything as HTML that can be used in a website. 
# Place the description in a <div> element.

# Technical specifications: ```{fact_sheet_chair}```
# """

# Guideline : Summarize - E-commerce reviews
# prod_review = """
# Got this panda plush toy for my daughter's birthday, \
# who loves it and takes it everywhere. It's soft and \ 
# super cute, and its face has a friendly look. It's \ 
# a bit small for what I paid though. I think there \ 
# might be other options that are bigger for the \ 
# same price. It arrived a day earlier than expected, \ 
# so I got to play with it myself before I gave it \ 
# to her.
# """

# prompt = f"""
# Your task is to generate a short summary of a product \
# review from an ecommerce site. 

# Summarize the review below, delimited by triple 
# backticks, in at most 30 words. 

# Review: ```{prod_review}```
# """

# ## Change the focus : Shipping department
# prompt = f"""
# Your task is to generate a short summary of a product \
# review from an ecommerce site to give feedback to the \
# Shipping deparmtment. 

# Summarize the review below, delimited by triple 
# backticks, in at most 30 words, and focusing on any aspects \
# that mention shipping and delivery of the product. 

# Review: ```{prod_review}```
# """

# ## Change the focus : Pricing department
# prompt = f"""
# Your task is to generate a short summary of a product \
# review from an ecommerce site to give feedback to the \
# pricing deparmtment, responsible for determining the \
# price of the product.  

# Summarize the review below, delimited by triple 
# backticks, in at most 30 words, and focusing on any aspects \
# that are relevant to the price and perceived value. 

# Review: ```{prod_review}```
# """

# ## Change the focus : product department
# prompt = f"""
# Your task is to generate a short summary of a product \
# review from an ecommerce site to give feedback to the \
# product deparmtment, responsible for determining the \
# quality of the product.  

# Summarize the review below, delimited by triple 
# backticks, in at most 30 words, and focusing on any aspects \
# that are relevant to the price and perceived value. 

# Review: ```{prod_review}```
# """

# ## Change the focus : supply chain department
# prompt = f"""
# Your task is to generate a short summary of a product \
# review from an ecommerce site to give feedback to the \
# supply chain department, responsible for determining the \
# quality of the packaging of the product.  

# Summarize the review below, delimited by triple 
# backticks, in at most 30 words, and focusing on any aspects \
# that are relevant to the price and perceived value. 

# Review: ```{prod_review}```
# """

# ## Guideline : Extract info

# prompt = f"""
# Your task is to extract relevant information from \ 
# a product review from an ecommerce site to give \
# feedback to the Shipping department. 

# From the review below, delimited by triple quotes \
# extract the information relevant to shipping and \ 
# delivery. Limit to 30 words. 

# Review: ```{prod_review}```
# """

# lamp_review = """
# Needed a nice lamp for my bedroom, and this one had \
# additional storage and not too high of a price point. \
# Got it fast.  The string to our lamp broke during the \
# transit and the company happily sent over a new one. \
# Came within a few days as well. It was easy to put \
# together.  I had a missing part, so I contacted their \
# support and they very quickly got me the missing piece! \
# Lumina seems to me to be a great company that cares \
# about their customers and products!!
# """

# prompt = f"""
# What is the sentiment of the following product review,
# which is delimited with triple backticks?

# Review text: '''{lamp_review}'''
# """

# prompt = f"""
# What is the sentiment of the following product review,
# which is delimited with triple backticks?

# Give your answer as as single word, either "positive" \
# or "negative"

# Review text: '''{lamp_review}'''
# """

# prompt = f"""
# Identify a list of emotions that the writer of the \
# following review is expressing. Include no more than \
# five items in the list. Format your answer as a list of \
# lower-case words separated by commas.

# Review text: '''{lamp_review}'''
# """

# prompt = f"""
# Is the writer of the following review expressing anger?\
# The review is delimited with triple backticks. \
# Give your answer as either yes or no.

# Review text: '''{lamp_review}'''
# """

# prompt = f"""
# Identify the following items from the review text: 
# - Item purchased by reviewer
# - Company that made the item

# The review is delimited with triple backticks. \
# Format your response as a JSON object with \
# "Item" and "Brand" as the keys. 
# If the information isn't present, use "unknown" \
# as the value.
# Make your response as short as possible.
  
# Review text: '''{lamp_review}'''
# """

# prompt = f"""
# Identify the following items from the review text: 
# - Sentiment (positive or negative)
# - Is the reviewer expressing anger? (true or false)
# - Item purchased by reviewer
# - Company that made the item

# The review is delimited with triple backticks. \
# Format your response as a JSON object with \
# "Sentiment", "Anger", "Item" and "Brand" as the keys.
# If the information isn't present, use "unknown" \
# as the value.
# Make your response as short as possible.
# Format the Anger value as a boolean.

# Review text: '''{lamp_review}'''
# """

# Guideline: Inferring

story = """
In a recent survey conducted by the government, 
public sector employees were asked to rate their level 
of satisfaction with the department they work at. 
The results revealed that NASA was the most popular 
department with a satisfaction rating of 95%.

One NASA employee, John Smith, commented on the findings, 
stating, "I'm not surprised that NASA came out on top. 
It's a great place to work with amazing people and 
incredible opportunities. I'm proud to be a part of 
such an innovative organization."

The results were also welcomed by NASA's management team, 
with Director Tom Johnson stating, "We are thrilled to 
hear that our employees are satisfied with their work at NASA. 
We have a talented and dedicated team who work tirelessly 
to achieve our goals, and it's fantastic to see that their 
hard work is paying off."

The survey also revealed that the 
Social Security Administration had the lowest satisfaction 
rating, with only 45% of employees indicating they were 
satisfied with their job. The government has pledged to 
address the concerns raised by employees in the survey and 
work towards improving job satisfaction across all departments.
"""

prompt = f"""
Determine five topics that are being discussed in the \
following text, which is delimited by triple backticks.

Make each item one or two words long. 

Format your response as a list of items separated by commas.

Text sample: '''{story}'''

"""

topic_list = [
    "nasa", "local government", "engineering", 
    "employee satisfaction", "federal government"
]

prompt = f"""
Determine whether each item in the following list of \
topics is a topic in the text below, which
is delimited with triple backticks.

Give your answer as list with 0 or 1 for each topic in a JSON format, 
key should be the topic and value should be the 0 or 1.\

List of topics: {", ".join(topic_list)}

Text sample: '''{story}'''
"""

response = get_completion(prompt)
print(response)