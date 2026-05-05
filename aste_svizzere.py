# ============================================
#   IL MIO PRIMO BACKEND PER ASTE SVIZZERE
# ============================================

from flask import Flask, jsonify, request

app = Flask(__name__)

auctions = [
    {"id": 1, "item": "Final Fantasy XVI - PS5 (sealed copy, mint condition)", "starting_price": 20, "current_bid": 20, "winner": None},
    {"id": 2, "item": "Rolex Submariner 1968 (vintage)",                       "starting_price": 5000, "current_bid": 5000, "winner": None},
    {"id": 3, "item": "Lindt 1879 Limited Edition Chocolate Box",              "starting_price": 80, "current_bid": 80, "winner": None},
]

# GET all auctions
@app.route("/auctions", methods=["GET"])
def get_auctions():
    return jsonify(auctions)

# POST a bid on an auction
@app.route("/auctions/<int:auction_id>/bid", methods=["POST"])
def place_bid(auction_id):
    auction = next((a for a in auctions if a["id"] == auction_id), None)
    if not auction:
        return jsonify({"error": "Auction not found"}), 404

    data    = request.get_json()
    bidder  = data.get("bidder")
    amount  = data.get("amount")

    if not bidder or not amount:
        return jsonify({"error": "Bidder and amount are required"}), 400

    if amount <= auction["current_bid"]:
        return jsonify({"error": f"Bid must be higher than {auction['current_bid']} CHF"}), 400

    auction["current_bid"] = amount
    auction["winner"]      = bidder

    return jsonify({
        "message": f"🏆 {bidder} is now winning!",
        "item":    auction["item"],
        "bid":     f"{amount} CHF"
    }), 200

# GET the winner of an auction
@app.route("/auctions/<int:auction_id>/winner", methods=["GET"])
def get_winner(auction_id):
    auction = next((a for a in auctions if a["id"] == auction_id), None)
    if not auction:
        return jsonify({"error": "Auction not found"}), 404

    if not auction["winner"]:
        return jsonify({"message": "No bids yet — be the first!"}), 200

    return jsonify({
        "item":   auction["item"],
        "winner": auction["winner"],
        "bid":    f"{auction['current_bid']} CHF"
    })

if __name__ == "__main__":
# ============================================
#   IL MIO PRIMO BACKEND PER ASTE SVIZZERE
# ============================================

from flask import Flask, jsonify, request

app = Flask(__name__)

auctions = [
    {"id": 1, "item": "Final Fantasy XVI - PS5 (sealed copy, mint condition)", "starting_price": 20, "current_bid": 20, "winner": None},
    {"id": 2, "item": "Rolex Submariner 1968 (vintage)",                       "starting_price": 5000, "current_bid": 5000, "winner": None},
    {"id": 3, "item": "Lindt 1879 Limited Edition Chocolate Box",              "starting_price": 80, "current_bid": 80, "winner": None},
]

# GET all auctions
@app.route("/auctions", methods=["GET"])
def get_auctions():
    return jsonify(auctions)

# POST a bid on an auction
@app.route("/auctions/<int:auction_id>/bid", methods=["POST"])
def place_bid(auction_id):
    auction = next((a for a in auctions if a["id"] == auction_id), None)
    if not auction:
        return jsonify({"error": "Auction not found"}), 404

    data    = request.get_json()
    bidder  = data.get("bidder")
    amount  = data.get("amount")

    if not bidder or not amount:
        return jsonify({"error": "Bidder and amount are required"}), 400

    if amount <= auction["current_bid"]:
        return jsonify({"error": f"Bid must be higher than {auction['current_bid']} CHF"}), 400

    auction["current_bid"] = amount
    auction["winner"]      = bidder

    return jsonify({
        "message": f"🏆 {bidder} is now winning!",
        "item":    auction["item"],
        "bid":     f"{amount} CHF"
    }), 200

# GET the winner of an auction
@app.route("/auctions/<int:auction_id>/winner", methods=["GET"])
def get_winner(auction_id):
    auction = next((a for a in auctions if a["id"] == auction_id), None)
    if not auction:
        return jsonify({"error": "Auction not found"}), 404

    if not auction["winner"]:
        return jsonify({"message": "No bids yet — be the first!"}), 200

    return jsonify({
        "item":   auction["item"],
        "winner": auction["winner"],
        "bid":    f"{auction['current_bid']} CHF"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
