import math


sample_text = """Before you can begin to determine what the composition of a particular paragraph will be, you must first decide on an argument and a working thesis statement for your paper. What is the most important idea that you are trying to convey to your reader? The information in each paragraph must be related to that idea. In other words, your paragraphs should remind your reader that there is a recurrent relationship between your thesis and the information in each paragraph. A working thesis functions like a seed from which your paper, and your ideas, will grow. The whole process is an organic one—a natural progression from a seed to a full-blown paper where there are direct, familial relationships between all of the ideas in the paper.

The decision about what to put into your paragraphs begins with the germination of a seed of ideas; this “germination process” is better known as brainstorming. There are many techniques for brainstorming; whichever one you choose, this stage of paragraph development cannot be skipped. Building paragraphs can be like building a skyscraper: there must be a well-planned foundation that supports what you are building. Any cracks, inconsistencies, or other corruptions of the foundation can cause your whole paper to crumble.

So, let’s suppose that you have done some brainstorming to develop your thesis. What else should you keep in mind as you begin to create paragraphs? Every paragraph in a paper should be:

    Unified: All of the sentences in a single paragraph should be related to a single controlling idea (often expressed in the topic sentence of the paragraph).
    Clearly related to the thesis: The sentences should all refer to the central idea, or thesis, of the paper (Rosen and Behrens 119).
    Coherent: The sentences should be arranged in a logical manner and should follow a definite plan for development (Rosen and Behrens 119).
    Well-developed: Every idea discussed in the paragraph should be adequately explained and supported through evidence and details that work together to explain the paragraph’s controlling idea (Rosen and Behrens 119).
"""


def deliverMessageViaCarrier(text, to, from_):
    """
    This function is responsible to trigger SMS.
    """
    # SmsCarrier.deliverMessage(text, to, from)
    return True


def sendSmsMessage(text, to, from_):
    """
    Assuming the max len of suffix text to be 16 char i.e 99 parts max
    the remaining char will be 144 (160 - 16).
    """
    start = 0
    initial = 1
    msg_chars = 144
    text_total_len = len(text)
    total_parts = math.ceil(text_total_len / msg_chars)
    while start < text_total_len:
        end_position = (initial * msg_chars)
        suffix = "\n- Part {} of {}".format(
            initial, total_parts)
        message_text = text[start: end_position] + suffix
        deliverMessageViaCarrier(
            message_text, to, from_)
        initial += 1
        start += msg_chars

# Uncomment the below code to test the function.
# sendSmsMessage(sample_text, 'to', 'from_')