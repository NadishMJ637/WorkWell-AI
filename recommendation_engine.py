"""
recommendation_engine.py

Recommendation engine for WorkWell AI.
"""

import json
import random

from config import RECOMMENDATION_FILE

from constants import (
    PRIORITY_HIGH,
    PRIORITY_CRITICAL,
    SENTIMENT_NEGATIVE
)


class RecommendationEngine:
    """
    Provides personalized wellness recommendations.
    """

    def __init__(self):

        self.recommendations = self.load()

    # =====================================================

    def load(self):
        """
        Load recommendation JSON.
        """

        try:

            with open(
                RECOMMENDATION_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)

        except FileNotFoundError:

            print("[ERROR] Recommendation file not found.")

            return {}

        except json.JSONDecodeError:

            print("[ERROR] Invalid recommendation JSON.")

            return {}

        except Exception as error:

            print(f"[ERROR] {error}")

            return {}

    # =====================================================

    def get_recommendations(
        self,
        intent,
        sentiment=None,
        priority=None
    ):
        """
        Return recommendations.
        """

        recommendations = self.recommendations.get(
            intent,
            []
        )

        # -----------------------------
        # Emergency Recommendation
        # -----------------------------

        if priority == PRIORITY_CRITICAL:

            return [

                "Please contact your manager or HR immediately.",

                "Reach out to the Employee Assistance Program.",

                "Talk with someone you trust."

            ]

        # -----------------------------

        if priority == PRIORITY_HIGH:

            recommendations = recommendations + [

                "Take a short break.",

                "Avoid multitasking."

            ]

        # -----------------------------

        if sentiment == SENTIMENT_NEGATIVE:

            recommendations = recommendations + [

                "Practice deep breathing for five minutes.",

                "Drink a glass of water.",

                "Take a short walk."

            ]

        # -----------------------------

        recommendations = list(

            dict.fromkeys(recommendations)

        )

        random.shuffle(recommendations)

        return recommendations[:5]


# ==========================================================
# Singleton
# ==========================================================

_engine = RecommendationEngine()


def get_recommendations(
    intent,
    sentiment=None,
    priority=None
):
    """
    Backward compatible wrapper.
    """

    return _engine.get_recommendations(

        intent,

        sentiment,

        priority

    )