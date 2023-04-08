import logging
from typing import Tuple

import opencc
import whisper
from whisper import Whisper


def transcribe_audio(
    whisper_model: Whisper, audio_input_file: str, txt_ouput_file: str, t2c_converter: opencc.OpenCC
) -> Tuple[dict, str]:
    logging.info(f"start transcribing..input file: {audio_input_file}.")
    result = whisper_model.transcribe(audio_input_file)
    if result.get("language", "") == "zh":
        with open(txt_ouput_file, mode="w", encoding="utf-8") as f:
            f.write("，".join([t2c_converter.convert(segment["text"]) for segment in result["segments"]]))
    else:
        with open(txt_ouput_file, mode="w", encoding="utf-8") as f:
            f.write(".".join([segment["text"] for segment in result["segments"]]))
    return result, txt_ouput_file


def load_model(model_checkpoint: str) -> Whisper:
    """
    should only be called once
    :param model_checkpoint:
    :return:
    """
    return whisper.load_model(model_checkpoint)
