--------------------------------------------------------------------------------
{-# LANGUAGE OverloadedStrings #-}
import           Data.Monoid (mappend)
import           Hakyll


--------------------------------------------------------------------------------
main :: IO ()
main = hakyllWith config $ do
    match "images/*" $ do
        route   idRoute
        compile copyFileCompiler

    match "css/*" $ do
        route   idRoute
        compile $ compressCssCompiler
            >>= relativizeUrls

    match "cgi/*" $ do
        route   $ gsubRoute "cgi/" (const "wedding/")
        compile copyFileCompiler

    match "pages/*" $ do
        route   $ gsubRoute "pages/" (const "wedding/") `composeRoutes` setExtension "html"
        compile $ pandocCompiler
            >>= loadAndApplyTemplate "templates/default.html" defaultContext
            >>= relativizeUrls

    match "index.html" $ do
        route idRoute
        compile copyFileCompiler

    match "templates/*" $ compile templateCompiler

--------------------------------------------------------------------------------
config :: Configuration
config = defaultConfiguration
    { deployCommand = "rsync --checksum -rv \
                      \_site/* menixon_ninjaartist@ssh.phx.nearlyfreespeech.net:/home/public/"
    }
