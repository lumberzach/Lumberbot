import discord
from discord.ext import commands
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


class HuluStreaming(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, Alases="Hulu")
    async def hulu(self, ctx):
        await ctx.send("Launching hulu... please wait until prompted to search")

        client = discord.Client()

        # loading webdrivers and opening the website
        options = Options()
        # Path to your chrome profile
        options.add_argument("user-data-dir=C:\\Users\\Boxca\\AppData\\Local\\Google\\Chrome\\profiletwo")
        driver = webdriver.Chrome(r"C:\Users\Boxca\Downloads\Drivers\chromedriver_win32 (1)\chromedriver.exe",
                                  options=options)
        driver.get('https://www.hulu.com/')

        time.sleep(5)

        # sign in
        try:
            element = driver.find_element_by_class_name('navigation__login-button').click()
            await ctx.send("We are logging in")
            email = driver.find_element_by_id('email_id')
            password = driver.find_element_by_id('password_id')
            login_button = driver.find_element_by_xpath("//button[@class='jsx-1761454348 login-button']")

            email.send_keys('boxcarracer0110@hotmail.com')
            password.send_keys('pn1567')
            login_button.click()

            time.sleep(5)

            try:
                # closing the modals
                welcome = WebDriverWait(driver, 4).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "WelcomeModal__cta"))
                )
                welcome.click()

                time.sleep(2)
                await ctx.send("Ready to search hulu")

            except NoSuchElementException:
                await ctx.send("Ready to search hulu")

            await ctx.send("Ready to search hulu")
        except NoSuchElementException:
            await ctx.send("type /search to search")

        time.sleep(2)



        driver.get('https://www.hulu.com/search')
        driver.find_element_by_css_selector('.cu-globalnav-search').click()
        search_box = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cu-search-input"))
        )

        await ctx.send("What do you want to watch?")
        msg = await self.bot.wait_for('message')
        search_query = msg.content

        search_box.send_keys(search_query)

        time.sleep(5)
        search_result_count = len(driver.find_elements_by_css_selector('li.InstantSearch__Option a'))
        await ctx.send(
            f"Please enter choice from 1 to {search_result_count}:") if search_result_count else print(
            "No result Found")

        for num, element in enumerate(driver.find_elements_by_css_selector('li.InstantSearch__Option a'),
                                      start=1):

            await ctx.send(f"Enter {num} for {element.text}")
        msg = await self.bot.wait_for('message')

        choice = int(msg.content)
        if search_result_count < choice:
            await ctx.send(f"Please enter only digits from 1 to {search_result_count}")

        javaScript = f"document.querySelectorAll('li.InstantSearch__Option a')[{choice - 1}].click();"
        driver.execute_script(javaScript)

        # playing the select option
        try:
            play_button = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.WatchAction a"))
            )

            play_button.click()




        except:
            await ctx.send("This video is restricted")

        finally:
            time.sleep(10)

        #performing searc














def setup(bot):
    bot.add_cog(HuluStreaming(bot))