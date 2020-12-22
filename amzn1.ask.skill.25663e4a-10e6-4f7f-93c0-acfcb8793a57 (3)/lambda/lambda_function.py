# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import random




import ask_sdk_core.utils as ask_utils
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_intent_name, get_dialog_state, get_slot_value
from ask_sdk_model import Response, DialogState



logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        #sid = SentimentIntensityAnalyzer()
        #sentiment_score = sid.polarity_scores(sentence)

        #positive_meter = round((sentiment_score['pos'] * 10), 2) 
        #negative_meter = round((sentiment_score['neg'] * 10), 2)

        # type: (HandlerInput) -> Response
        speak_output = ("Hello, I am alexa teddy bear, I am here to listen. "
                        "How are you doing?")

        reprompt = "How are you doing? "

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt)
                .response
        )


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BeginningIntent")(handler_input)

    def handle(self, handler_input):
        #type: (HandlerInput) -> Response
        greet = ["Hello, im doing great myself, anything on your mind?","Im here to lsiten ","Tell me how you are doing today"]
        n = random.randint(0,3)
        speak_output = greet[n]
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class BadIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BadIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        bad =["Hey, everything is giong to be okay just focus on you", "Sometimes you just gotta start over from the basics, whats causing you trouble ?", "I do believe that you future will be bright, don't let these things bother you", "Dont stress yourself out tell me, lets whats going on, how do you feel "]
        n = random.randint(0,2)
        
            
            
        speak_output = bad[n] 

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )




class GoodIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GoodIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        good =["Awesome, it is always great to feel that positivity, do you still want to talk", "I'm glad that you're happy, don't forget to do you homework for ward", "It's always nice to hear people filled with joy, do you want to continue/"]
        n = random.randint(0,2)
        
            
            
        speak_output = good[n] 

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )





class LostIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("LostIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        lost =["Hey, sometimes its okay to be confused and don't give up", "Someitmes you have to look at the positivity in life", "Don't get so caught with life's pressures"]
        n = random.randint(0,2)
        
            
            
        speak_output = lost[n] 

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
                
                
        )



class YesIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("YesIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        yes =["I'm always ready to lsiten ", "of course how are you feeling ", "Tell me what is on your mind  "]
        n = random.randint(0,2)
        
            
            
        speak_output = yes[n] 

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )






class NoIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        no =["Well my job is done, bye! ", "If you need anyting give me a call ", "Have a good day  "]
        n = random.randint(0,2)
        
            
            
        speak_output = no[n] 

        return (
            handler_input.response_builder
                .speak(speak_output)
            
                .response
        )




class ThankIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ThankIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        yes =["You are welcome do you still want to talk  ", "of course how are you feeling ", "Yes anything else you want to share  "]
        n = random.randint(0,2)
        
            
            
        speak_output = yes[n] 

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )




class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(BadIntentHandler())
sb.add_request_handler(GoodIntentHandler())
sb.add_request_handler(LostIntentHandler())
sb.add_request_handler(YesIntentHandler())
sb.add_request_handler(NoIntentHandler())
sb.add_request_handler(ThankIntentHandler())

sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()