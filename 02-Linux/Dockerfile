FROM ubuntu:24.04

# 1. Εγκατάσταση βασικών εργαλείων που μπορεί να χρειαστούν οι παίκτες (π.χ. curl, xxd, nano, κλπ)
RUN apt-get update && apt-get install -y \
    sudo \
    curl \
    nano \
    vim \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 2. Δημιουργία του χρήστη "player" με password "player"
RUN useradd -m -s /bin/bash player && \
    echo "player:player" | chpasswd && \
    usermod -aG sudo player

# 3. Ρύθμιση ώστε ο "player" να τρέχει sudo ΧΩΡΙΣ να ζητάει password
RUN echo "player ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# 4. Αντιγραφή όλων των challenges μέσα στον φάκελο του player
COPY linux_challenges/ /home/player/linux_challenges/
# Αντιγραφή του setup.sh μέσα στο container
COPY configs/setup.sh /root/setup.sh
COPY configs/uninstall.sh /root/uninstall.sh
COPY configs/redeem /root/redeem

# 2. Δίνουμε δικαιώματα εκτέλεσης στα scripts
RUN chmod +x /root/setup.sh

WORKDIR /root

RUN ./setup.sh

# 5. Ρύθμιση σωστών δικαιωμάτων
RUN chown -R root:root /home/player/linux_challenges && \
    chmod -R 755 /home/player/linux_challenges

# 6. Ορισμός αρχικού φακέλου και χρήστη κατά την είσοδο
WORKDIR /home/player
USER player

# 7. Ξεκινάει απευθείας ένα Bash shell για τον παίκτη
CMD ["/bin/bash"]
