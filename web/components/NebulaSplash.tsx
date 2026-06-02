"use client";

import { motion, AnimatePresence } from "framer-motion";
import { useEffect } from "react";

interface NebulaSplashProps {
  /** Callback quand l'utilisateur clique pour entrer */
  onDismiss: () => void;
}

/**
 * Splash d'amorce premium : image NEBULA en background opacite reduite,
 * titre serif italic geant qui fade-in, "CLICK ANYWHERE TO ENTER" qui clignote.
 * Click anywhere ou touche clavier (Enter / Space) -> dismiss.
 */
export default function NebulaSplash({ onDismiss }: NebulaSplashProps) {
  useEffect(() => {
    const handleKey = (e: KeyboardEvent) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        onDismiss();
      }
    };
    window.addEventListener("keydown", handleKey);
    return () => window.removeEventListener("keydown", handleKey);
  }, [onDismiss]);

  return (
    <AnimatePresence>
      <motion.div
        key="splash"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        transition={{ duration: 0.6 }}
        onClick={onDismiss}
        className="fixed inset-0 z-[9999] flex cursor-pointer flex-col items-center justify-center bg-charcoal"
      >
        {/* Image NEBULA en background, opacite reduite */}
        <div
          className="absolute inset-0 bg-cover bg-center"
          style={{
            backgroundImage: "url(/textures/nebula-bg.png)",
            opacity: 0.18,
            filter: "blur(1px) hue-rotate(310deg) saturate(0.8)",
          }}
        />

        {/* Overlay gradient charcoal pour assombrir et donner de la profondeur */}
        <div
          className="absolute inset-0"
          style={{
            background:
              "radial-gradient(ellipse at center, transparent 0%, rgba(45,42,38,0.6) 70%, rgba(45,42,38,0.95) 100%)",
          }}
        />

        {/* Texture noise tres subtile */}
        <div
          className="pointer-events-none absolute inset-0 opacity-30"
          style={{
            backgroundImage:
              "url(\"data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.06 0'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)'/%3E%3C/svg%3E\")",
          }}
        />

        {/* Particules / etoiles subtle */}
        <div className="pointer-events-none absolute inset-0">
          {Array.from({ length: 30 }).map((_, i) => (
            <motion.div
              key={i}
              className="absolute h-px w-px rounded-full bg-creme"
              style={{
                top: `${(i * 37) % 100}%`,
                left: `${(i * 71) % 100}%`,
                boxShadow: "0 0 4px rgba(250, 247, 242, 0.6)",
              }}
              animate={{
                opacity: [0.2, 0.9, 0.2],
              }}
              transition={{
                duration: 2 + (i % 4),
                repeat: Infinity,
                delay: i * 0.1,
                ease: "easeInOut",
              }}
            />
          ))}
        </div>

        {/* Contenu central */}
        <div className="relative z-10 flex flex-col items-center px-8 text-center">
          {/* Kicker eyebrow */}
          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.4 }}
            className="mb-8 text-[0.65rem] font-medium uppercase tracking-[0.5em] text-terracotta"
          >
            — Édition Première — 2026 —
          </motion.div>

          {/* Titre principal */}
          <motion.h1
            initial={{ opacity: 0, scale: 0.95, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            transition={{
              duration: 1.2,
              delay: 0.6,
              ease: [0.25, 0, 0, 1],
            }}
            className="font-serif text-[clamp(4rem,11vw,9rem)] italic leading-[0.92] tracking-[-0.04em] text-creme"
            style={{
              textShadow:
                "0 0 60px rgba(201, 123, 95, 0.3), 0 0 120px rgba(201, 123, 95, 0.15)",
            }}
          >
            NutriRecettes
          </motion.h1>

          {/* Tagline */}
          <motion.p
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 1.4 }}
            className="mt-4 font-serif text-lg italic text-creme/70 sm:text-xl"
          >
            La cuisine du monde, à portée d&apos;un geste.
          </motion.p>

          {/* Divider */}
          <motion.div
            initial={{ width: 0, opacity: 0 }}
            animate={{ width: 80, opacity: 1 }}
            transition={{ duration: 1, delay: 1.8 }}
            className="mt-10 h-px bg-gradient-to-r from-transparent via-terracotta to-transparent"
          />

          {/* CTA enter */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.6, delay: 2.2 }}
            className="mt-12 flex items-center gap-4"
          >
            <motion.span
              animate={{ opacity: [0.4, 1, 0.4] }}
              transition={{
                duration: 2,
                repeat: Infinity,
                ease: "easeInOut",
              }}
              className="text-[0.7rem] font-medium uppercase tracking-[0.4em] text-creme/80"
            >
              <span className="text-terracotta">●</span>{" "}
              <span className="mx-3">Cliquez n&apos;importe où pour entrer</span>{" "}
              <span className="text-terracotta">●</span>
            </motion.span>
          </motion.div>
        </div>

        {/* Footer copyright bas */}
        <div className="absolute bottom-6 left-1/2 -translate-x-1/2 text-[0.6rem] uppercase tracking-[0.4em] text-creme/40">
          © 2026 NutriRecettes — un carnet de cuisine
        </div>
      </motion.div>
    </AnimatePresence>
  );
}
